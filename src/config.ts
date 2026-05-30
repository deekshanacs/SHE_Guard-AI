// Use Vite environment variable `VITE_API_BASE_URL` when provided.
// If not set, default to same-origin (empty string) so SPA rewrite can proxy calls.
const API_BASE_URL = (import.meta as any).env?.VITE_API_BASE_URL ?? "";

export const apiUrl = (path: string) => {
  const normalizedPath = path.startsWith("/") ? path : `/${path}`;
  return `${API_BASE_URL}${normalizedPath}`;
};

