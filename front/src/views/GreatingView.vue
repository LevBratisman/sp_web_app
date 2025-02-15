<template>
    <div class="greeting-content">
        <v-img v-if="theme.global.name.value == 'dark'" :src="require('@/ava_light.png')"></v-img>
        <v-img v-else :src="require('@/ava_dark.png')"></v-img>
        <div class="nav-arrow">
            <v-icon icon="mdi-arrow-down-thick"></v-icon>
        </div>
    </div>
</template>

<script setup>
    import { useTheme } from 'vuetify';

    const theme = useTheme();

</script>

<style scoped>

    @keyframes appear{
        0%{
            opacity:0;
        }
        100% {
            opacity:1;
            transform: scale(1);
        }
    }

    @keyframes arrow-nav{
        0% {
            opacity: 0;
        }
        20% {
            opacity: 0;
        }
        30% {
            opacity: 1;
        }
        40% {
            opacity: 1;
            transform: translateY(10px);
        }
        60% {
            opacity: 1;
            transform: translateY(-10px);
        }
        80% {
            opacity: 1;
            transform: translateY(10px);
        }
        100% {
            transform: translateY(-10px);
        }
    }

    .greeting-content {
        opacity: 0;
        transition: 1s;
        animation: appear 1s 1;
        animation-fill-mode: forwards;
        transform: scale(0.9);

        height: calc(100vh - 120px);
        display: flex;
        justify-content: center;
    }

    .nav-arrow {
        opacity: 0;
        transition: 1s;
        animation: arrow-nav 5s infinite;
        transform: translateY(-40px);
        position: fixed;
        bottom: 20px;
        z-index: 999;
    }

</style>