import { flushPromises, mount } from "@vue/test-utils";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import HomeView from "../src/views/HomeView.vue";

describe("HomeView", () => {
    beforeEach(() => {
        window.pywebview = {
            api: {
                app: {
                    getVersion: vi.fn().mockResolvedValue("1.0.0"),
                },
                greeting: {
                    sayHello: vi.fn().mockResolvedValue(undefined),
                },
            },
        };
    });

    afterEach(() => {
        vi.restoreAllMocks();
    });

    it("renders the version from app after pywebviewready", async () => {
        const wrapper = mount(HomeView);
        window.dispatchEvent(new Event("pywebviewready"));
        await flushPromises();
        expect(wrapper.text()).toContain("1.0.0");
    });

    it("shows empty input initially", () => {
        const wrapper = mount(HomeView);
        const input = wrapper.find("input");
        expect(input.exists()).toBe(true);
        expect((input.element as HTMLInputElement).value).toBe("");
    });

    it("renders the Send button", () => {
        const wrapper = mount(HomeView);
        const button = wrapper.find("button");
        expect(button.exists()).toBe(true);
        expect(button.text()).toBe("Send");
    });

    it("calls greeting.sayHello on button click", async () => {
        const wrapper = mount(HomeView);
        const input = wrapper.find("input");
        await input.setValue("test message");

        const button = wrapper.find("button");
        await button.trigger("click");

        expect(window.pywebview.api.greeting.sayHello).toHaveBeenCalledWith("test message");
    });

    it("listens for pywebviewready and greeting:hello on mount", async () => {
        const addEventListenerSpy = vi.spyOn(window, "addEventListener");
        mount(HomeView);
        await flushPromises();
        expect(addEventListenerSpy).toHaveBeenCalledWith("pywebviewready", expect.any(Function));
        expect(addEventListenerSpy).toHaveBeenCalledWith("greeting:hello", expect.any(Function));
    });

    it("displays message when greeting:hello event is received", async () => {
        const wrapper = mount(HomeView);
        await flushPromises();

        window.dispatchEvent(new CustomEvent("greeting:hello", { detail: "Hello, World" }));
        await wrapper.vm.$nextTick();

        expect(wrapper.text()).toContain("Hello, World");
    });
});
