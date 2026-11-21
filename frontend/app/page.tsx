"use client";

import { useEffect, useState, type FormEvent } from "react";

type Org = { id: string; name: string; role: string };
type Workspace = { id: string; name: string; organization_id: string };
type Project = { id: string; title: string; organization_id: string; workspace_id: string };
type Item = { id: string; title: string; status: string; project_id: string };
type Member = { id: string; username: string; role: string; active: boolean };
type Scope = { org: Org; workspace: Workspace };

const A_PROJECT = "aaaaaaaa-aaaa-4aaa-cccc-aaaaaaaaaaaa";
const B_PROJECT = "bbbbbbbb-bbbb-4bbb-cccc-bbbbbbbbbbbb";
const B_ORG = "bbbbbbbb-bbbb-4bbb-bbbb-bbbbbbbbbbbb";

function csrfToken(): string {
  const entry = document.cookie.split("; ").find((c) => c.startsWith("csrftoken="));
  return entry ? decodeURIComponent(entry.substring("csrftoken=".length)) : "";
}

async function call<T>(path: string, method = "GET", payload?: object): Promise<T> {
  const response = await fetch(path, {
    method,
    credentials: "same-origin",
    cache: "no-store",
    headers: {
      "Content-Type": "application/json",
      ...(method !== "GET" ? { "X-CSRFToken": csrfToken() } : {}),
    },
    ...(payload === undefined ? {} : { body: JSON.stringify(payload) }),
  });
  const parsed: unknown = await response.json();
  if (!response.ok) {
    const obj = (parsed && typeof parsed === "object") ? parsed as { detail?: string } : {};
    throw new Error("HTTP " + response.status + ": " + (obj.detail || "requête refusée"));
  }
  return parsed as T;
}

export default function Home() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [loggedIn, setLoggedIn] = useState<string | null>(null);
  const [orgs, setOrgs] = useState<Org[]>([]);
  const [scope, setScope] = useState<Scope | null>(null);
  const [projects, setProjects] = useState<Project[]>([]);
  const [items, setItems] = useState<Item[]>([]);
  const [members, setMembers] = useState<Member[]>([]);
  const [newProject, setNewProject] = useState("");
  const [newItem, setNewItem] = useState("");
  const [notice, setNotice] = useState("Jeux de données fictifs uniquement.");
  const [busy, setBusy] = useState(false);

  async function getOrgs() {
    const res = await call<{ organizations: Org[] }>("/api/organizations/");
    setOrgs(res.organizations);
  }

  async function openScope(org: Org) {
    setBusy(true);
    try {
      const w = await call<{ workspaces: Workspace[] }>("/api/workspaces/?organization_id=" + org.id);
      if (!w.workspaces.length) throw new Error("Aucun Workspace autorisé");
      const workspace = w.workspaces[0];
      await call("/api/context/", "POST", { organization_id: org.id, workspace_id: workspace.id });
      setScope({ org, workspace });
      const p = await call<{ projects: Project[] }>("/api/projects/");
      const i = await call<{ workitems: Item[] }>("/api/workitems/");
      setProjects(p.projects);
      setItems(i.workitems);
      if (org.role === "owner" || org.role === "admin") {
        const m = await call<{ memberships: Member[] }>("/api/memberships/");
        setMembers(m.memberships);
      } else setMembers([]);
      setNotice("Contexte validé : " + org.name + " / " + workspace.name);
    } catch (error) {
      setScope(null);
      setNotice(String(error));
    } finally {
      setBusy(false);
    }
  }

  useEffect(() => {
    void (async () => {
      try {
        await call("/api/auth/csrf/");
        const me = await call<{ username: string }>("/api/me/");
        setLoggedIn(me.username);
        await getOrgs();
      } catch { setLoggedIn(null); }
    })();
  }, []);

  async function login(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    setBusy(true);
    try {
      await call("/api/auth/csrf/");
      const result = await call<{ username: string }>("/api/auth/login/", "POST", { username, password });
      setLoggedIn(result.username);
      setPassword("");
      await getOrgs();
      setNotice("Choisis explicitement ton Organization et ton Workspace.");
    } catch (error) { setNotice(String(error)); }
    finally { setBusy(false); }
  }

  async function logout() {
    try { await call("/api/auth/logout/", "POST", {}); } catch { /* Session may have expired. */ }
    setLoggedIn(null); setScope(null); setProjects([]); setItems([]); setOrgs([]);
    setNotice("Session terminée.");
  }

  async function createProject(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (!scope || !newProject.trim()) return;
    try {
      await call("/api/projects/", "POST", { title: newProject });
      setNewProject("");
      await openScope(scope.org);
    } catch (error) { setNotice(String(error)); }
  }

  async function createItem(e: FormEvent<HTMLFormElement>) {
    e.preventDefault();
    if (!scope || !newItem.trim() || !projects.length) return;
    try {
      await call("/api/workitems/", "POST", { title: newItem, project_id: projects[0].id });
      setNewItem("");
      await openScope(scope.org);
    } catch (error) { setNotice(String(error)); }
  }

  async function testIsolation() {
    if (!scope) return;
    const forbidden = scope.org.id === B_ORG ? A_PROJECT : B_PROJECT;
    try {
      await call("/api/projects/" + forbidden + "/");
      setNotice("ERREUR : le serveur a autorisé une lecture étrangère.");
    } catch (error) {
      setNotice(String(error).includes("HTTP 404")
        ? "TEST PASS : ressource de l'autre tenant invisible (HTTP 404)."
        : "Résultat du test : " + String(error));
    }
  }

  async function testMandate() {
    try {
      await call("/api/approvals/", "POST", { decision_id: "synthetic" });
      setNotice("ERREUR : approbation sans mandat autorisée.");
    } catch (error) {
      setNotice(String(error).includes("HTTP 403")
        ? "TEST PASS : approbation sans mandat refusée (HTTP 403)."
        : "Résultat du test : " + String(error));
    }
  }

  async function revoke() {
    if (!scope) return;
    const target = members.find((m) => m.username === "demo_revoke" && m.active);
    if (!target) { setNotice("Membre de test absent ou déjà révoqué."); return; }
    try {
      await call("/api/memberships/" + target.id + "/revoke/", "POST", {});
      await openScope(scope.org);
      setNotice("Membership de demo_revoke révoqué ; une session ancienne perd ses droits.");
    } catch (error) { setNotice(String(error)); }
  }

  async function exportScope() {
    try {
      const data = await call<object>("/api/export/");
      const url = URL.createObjectURL(new Blob([JSON.stringify(data, null, 2)], { type: "application/json" }));
      const a = document.createElement("a");
      a.href = url; a.download = "projecthub-e0-synthetic.json"; a.click();
      URL.revokeObjectURL(url);
      setNotice("Export synthétique borné au contexte courant.");
    } catch (error) { setNotice(String(error)); }
  }

  const admin = scope?.org.role === "owner" || scope?.org.role === "admin";
  const canWrite = !!scope && (admin || loggedIn !== "demo_viewer");

  return (
    <main>
      <header className="hero">
        <div className="brand"><span className="cube" aria-hidden="true">⬡</span> ProjectHub <small>E0</small></div>
        <div className="overline">ARCHITECTURE &amp; ENGINEERING · SLICE-00</div>
        <h1>Isolation multi-tenant, <em>observable.</em></h1>
        <p>Démonstrateur Django/DRF + Next.js + PostgreSQL. Deux organisations fictives, droits explicites et refus côté serveur.</p>
        <div className="flags"><span>DONNÉES SYNTHÉTIQUES</span><span>ADR NON APPROUVÉS</span><span>E1 : NO-GO</span></div>
      </header>
      <section className="notice" aria-live="polite">{notice}</section>

      {!loggedIn ? (
        <section className="panel auth">
          <div>
            <h2>Connexion E0</h2>
            <p>Utilisateurs fictifs : <code>demo_alice</code>, <code>demo_admin_a</code>, <code>demo_both</code>, <code>demo_viewer</code>.</p>
            <p>Mot de passe des fixtures : défini par <code>E0_DEMO_PASSWORD</code>, sinon valeur publique reconstruite.</p>
            <p className="muted">Aucun compte ni document réel.</p>
          </div>
          <form onSubmit={login}>
            <label htmlFor="user">Identifiant fictif</label>
            <input id="user" required value={username} onChange={(e) => setUsername(e.target.value)} autoComplete="username" />
            <label htmlFor="pass">Mot de passe de démo</label>
            <input id="pass" required type="password" value={password} onChange={(e) => setPassword(e.target.value)} autoComplete="current-password" />
            <button type="submit" disabled={busy}>Se connecter</button>
          </form>
        </section>
      ) : (
        <>
          <div className="toolbar"><span>Session fictive : <strong>{loggedIn}</strong></span><button onClick={logout} className="secondary">Déconnexion</button></div>
          <section className="panel">
            <h2>01 · Contexte tenant explicite</h2>
            <p>Un membership dans A ne donne aucun droit automatique dans B.</p>
            <div className="cards">
              {orgs.map((org) => (
                <button key={org.id} disabled={busy} className={"org " + (scope?.org.id === org.id ? "selected" : "")} onClick={() => void openScope(org)}>
                  <strong>{org.name}</strong><span>Rôle : {org.role}</span><span>{scope?.org.id === org.id ? "Actif" : "Sélectionner"}</span>
                </button>
              ))}
            </div>
          </section>
          {scope && (
            <>
              <section className="panel">
                <h2>02 · {scope.workspace.name} : données visibles</h2>
                <div className="two-cols">
                  <div>
                    <h3>Projects fictifs</h3>
                    <ul>{projects.map((p) => <li key={p.id}>{p.title}</li>)}</ul>
                    {canWrite && <form className="inline" onSubmit={createProject}><label htmlFor="project">Nouveau Project fictif</label><input id="project" value={newProject} onChange={(e) => setNewProject(e.target.value)} /><button type="submit">Créer</button></form>}
                  </div>
                  <div>
                    <h3>WorkItems fictifs</h3>
                    <ul>{items.map((i) => <li key={i.id}>{i.title} <span className="muted">({i.status})</span></li>)}</ul>
                    {canWrite && projects.length > 0 && <form className="inline" onSubmit={createItem}><label htmlFor="item">Nouvelle action fictive</label><input id="item" value={newItem} onChange={(e) => setNewItem(e.target.value)} /><button type="submit">Créer</button></form>}
                  </div>
                </div>
              </section>
              <section className="panel">
                <h2>03 · Scénarios de refus et de révocation</h2>
                <div className="cards action-cards">
                  <button className="secondary" onClick={testIsolation}>Lire un Project étranger (404)</button>
                  <button className="secondary" onClick={testMandate}>Approuver sans mandat (403)</button>
                  <button className="secondary" onClick={exportScope}>Exporter seulement ce tenant</button>
                  {admin && <button className="secondary" onClick={revoke}>Révoquer demo_revoke</button>}
                </div>
                <p className="muted">Ces vérifications sont réalisées par l'API et non par une condition de rendu React.</p>
              </section>
            </>
          )}
        </>
      )}
      <footer>ProjectHub 2026 · E0 expérimental, aucune donnée réelle · E1 : NO-GO</footer>
    </main>
  );
}
