import type { Metadata } from "next";
import type { ReactNode } from "react";
import "./globals.css";

export const metadata: Metadata = {
  title: "ProjectHub | Démonstrateur E0",
  description: "Démonstration fictive SLICE-00 : isolation, scopes, refus et révocation.",
  robots: { index: false, follow: false },
};

export default function Layout({ children }: { children: ReactNode }) {
  return <html lang="fr"><body>{children}</body></html>;
}
