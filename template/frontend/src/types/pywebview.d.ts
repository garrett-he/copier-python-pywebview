interface AppBridge {
    getVersion(): Promise<string>;
}

interface GreetingBridge {
    sayHello(name: string): Promise<void>;
}

interface JsApi {
    app: AppBridge;
    greeting: GreetingBridge;
}

interface Pywebview {
    api: JsApi;
}

declare global {
    interface Window {
        pywebview: Pywebview;
    }
}

export type { AppBridge, GreetingBridge, JsApi };
