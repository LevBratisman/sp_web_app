<template>
    <div class="user-layout-wrapper">
        <Header v-if="route.path == '/'" class="header" title="SIMPLE PHYSICS"></Header>
        <Header v-else title="SIMPLE PHYSICS"></Header>

        <div v-if="route.path == '/'" class="greeting-content">
            <img v-if="theme.global.name.value == 'dark'" class="img" src="../../public/ava_light.png"></img>
            <img v-else class="img" src="../../public/ava_dark.png"></img>
            <div class="nav-arrow">
                <v-icon icon="mdi-arrow-down-thick"></v-icon>
            </div>
        </div>

        <div class="user-layout-navbar">
            <NavBar></NavBar>
        </div>
    </div>
</template>

<script setup lang="ts">
    import NavBar from '../components/NavBar.vue';
    import Header from '../components/Header.vue';
    import { useTheme } from 'vuetify';
    import { useRoute } from 'vue-router';

    const route = useRoute();
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

    @keyframes header-show{
        0%{
            transform: translateY(-100px);
        }
        100% {
            opacity: 1;
            transform: translateY(0);
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

    .user-layout-wrapper {
        height: calc(100vh - 120px);
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
        padding: 0 20px;
    }

    .nav-arrow {
        opacity: 0;
        transition: 1s;
        animation: arrow-nav 5s 1s infinite;
        transform: translateY(-40px);
        position: fixed;
        bottom: 20px;
        z-index: 999;
    }

    .header {
        opacity: 0;
        animation: header-show 1s 1s 1;
        animation-fill-mode: forwards;
    }

    .img { 
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: contain;
    }

</style>