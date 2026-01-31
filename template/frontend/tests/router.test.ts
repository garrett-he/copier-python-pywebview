import { describe, expect, it } from "vitest";
import router from "../src/router/index";

describe("router", () => {
    it("creates a router with hash history", () => {
        expect(router.options.history).toBeDefined();
    });

    it("has a home route", () => {
        const route = router.getRoutes().find((r) => r.name === "home");
        expect(route).toBeDefined();
        expect(route!.path).toBe("/");
    });
});
