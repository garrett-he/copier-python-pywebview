<script setup lang="ts">
import { onMounted, onUnmounted, ref } from "vue";
import { useApi } from "@/composables/useApi";

const api = useApi();
const version = ref("");
const message = ref("");
const input = ref("");

function onHelloEvent(event: Event): void {
    const detail = (event as CustomEvent<string>).detail;
    message.value = detail;
}

async function init(): Promise<void> {
    version.value = await api.app.getVersion();
}

// biome-ignore lint/correctness/noUnusedVariables: used in template
async function callSayHello(): Promise<void> {
    await api.greeting.sayHello(input.value);
}

onMounted(() => {
    window.addEventListener("pywebviewready", init);
    window.addEventListener("greeting:hello", onHelloEvent);
});

onUnmounted(() => {
    window.removeEventListener("pywebviewready", init);
    window.removeEventListener("greeting:hello", onHelloEvent);
});
</script>

<template>
    <main>
        <p>App Version: {{ version }}</p>
        <p>
            Your Name: <input v-model="input" placeholder="Enter a message" />
            <button @click="callSayHello">Send</button>
        </p>
        <p>{{ message }}</p>
    </main>
</template>
