import type { NextConfig } from "next";

const backend = process.env.BACKEND_INTERNAL_URL || "http://127.0.0.1:8000";
const config: NextConfig = {
  reactStrictMode: true,
  skipTrailingSlashRedirect: true,
  async rewrites() {
    return [{ source: "/api/:path*", destination: backend + "/api/:path*" }];
  },
};

export default config;
