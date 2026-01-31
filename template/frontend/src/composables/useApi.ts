import type { JsApi } from "@/types/pywebview";

export function useApi(): JsApi {
    return new Proxy({} as JsApi, {
        get(_, prop: keyof JsApi) {
            return window.pywebview?.api[prop];
        },
    });
}
