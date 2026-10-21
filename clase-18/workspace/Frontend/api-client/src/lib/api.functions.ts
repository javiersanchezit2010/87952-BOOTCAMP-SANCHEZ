import { createServerFn } from "@tanstack/react-start";

export type Alumno = {
  legajo?: number;
  nombre: string;
  apellido: string;
  fechaDeNacimiento: string;
};

const headers = {
  "Content-Type": "application/json",
  "X-Tunnel-Skip-AntiPhishing-Page": "true",
};

function buildUrl(base: string, path: string) {
  const url = new URL(path, base.endsWith("/") ? base : base + "/");
  if (url.protocol !== "https:" && url.protocol !== "http:") throw new Error("URL inválida");
  return url.toString();
}

async function parse(res: Response) {
  const text = await res.text();
  if (!res.ok) throw new Error(`Error ${res.status}: ${text.slice(0, 200)}`);
  try {
    return JSON.parse(text);
  } catch {
    return text;
  }
}

export const apiGet = createServerFn({ method: "POST" })
  .validator((d: { base: string; path: string }) => d)
  .handler(async ({ data }) => {
    const res = await fetch(buildUrl(data.base, data.path), { headers });
    return (await parse(res)) as Alumno | Alumno[];
  });

export const apiPost = createServerFn({ method: "POST" })
  .validator((d: { base: string; alumno: Alumno }) => d)
  .handler(async ({ data }) => {
    const res = await fetch(buildUrl(data.base, "alumnos"), {
      method: "POST",
      headers,
      body: JSON.stringify(data.alumno),
    });
    return JSON.stringify(await parse(res));
  });
