// Always use same-origin `/api` so localhost and Render both rely on routing
// instead of hardcoding the backend host into the browser bundle.
export const API_BASE_URL = "";

export const apiUrl = (path: string) => {
  const normalizedPath = path.startsWith("/") ? path : `/${path}`;
  return `${API_BASE_URL}${normalizedPath}`;
};

