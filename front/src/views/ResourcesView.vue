<template>
    <div class="resources-wrapper">
        <div class="resources-block">

            <div class="flex-double-block">
                <a href="https://t.me/simplephysics_polyteh" target=»_blank>
                    <div class="telegram-block">
                        <v-img v-if="theme.global.name.value == 'light'" src="tg_icon.svg"></v-img>
                        <v-img v-else src="tg_icon_white.png"></v-img>
                    </div>
                </a>
            </div>
            <div class="flex-double-block">
                <a href="https://t.me/simplephysicsbot" target=»_blank>
                    <div class="link-block telegram-bot-block">
                        <v-icon v-if="theme.global.name.value == 'light'" icon="mdi-robot"></v-icon>
                        <v-icon v-else class="link-dark" icon="mdi-robot"></v-icon>
                    </div>
                </a>
                <a href="https://vk.com/simplephysicsmp" target=»_blank>
                    <div class="link-block vk-group-block">
                        <v-img v-if="theme.global.name.value == 'light'" src="vk_icon.png"></v-img>
                        <v-img v-else src="vk_icon_white.png"></v-img>
                    </div>
                </a>
            </div>
            <div class="flex-double-block">
                <a href="https://www.youtube.com/@Simplephysics-mpu" target=»_blank>
                    <div class="link-block youtube-block">
                        <v-icon v-if="theme.global.name.value == 'light'" icon="mdi-youtube"></v-icon>
                        <v-icon v-else class="link-dark" icon="mdi-youtube"></v-icon>
                    </div>
                </a>
                <a href="https://rutube.ru/channel/43627801/shorts/" target=»_blank>
                    <div class="link-block rutube-block">
                        <v-icon v-if="theme.global.name.value == 'light'" icon="mdi-alpha-r-box"></v-icon>
                        <v-icon v-else class="link-dark" icon="mdi-alpha-r-box"></v-icon>
                    </div>
                </a>
            </div>

            <div class="nav-tip">
                <div class="nav-tip-arrow">
                    <v-icon icon="mdi-arrow-up-thin"></v-icon>
                </div>
                <p class="nav-tip-title">Переходи по ссылкам</p>
            </div>

        </div>
    </div>
</template>

<script setup lang="ts">

    import { useTheme } from 'vuetify';

    const theme = useTheme();

</script>

<style scoped>

    @keyframes telegram-show{
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @keyframes telegram-bot-show{
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @keyframes youtube-show{
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @keyframes rutube-show{
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @keyframes vk-group-show{
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @keyframes nav-title-show{
        0% {
            opacity: 0;
        }
        100% {
            opacity: 0.5;
        }
    }

    @keyframes nav-arrow-show{
        0% {
            opacity: 0;
        }
        100% {
            opacity: 0.5;
            transform: translateY(-10px);
        }
    }

    a {
        color: #000;
        text-decoration: none
    }

    .link-dark {
        color: #fff;
    }

    .resources-wrapper {
        height: calc(100vh - 120px);
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .resources-block {
        display: flex;
        flex-direction: column;
        gap: 20px;
    }

    .flex-double-block {
        display: flex;
        gap: 20px;
    }

    .link-block {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 120px;
        width: 120px;
        border-radius: 10px;
        padding: 20px;
        font-size: 60px;
        cursor: pointer;
        transition: 0.5s;
    }

    .link-block:hover {
        box-shadow: 0px 5px 84px 36px rgba(14, 25, 34, 0.3) inset;
    }

    .telegram-block {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 120px;
        width: 260px;
        border-radius: 10px;
        padding: 20px;
        cursor: pointer;
        transition: 0.5s;
        background-color: rgb(107, 147, 249);
        opacity: 0;


        animation: telegram-show 1s 1;
        animation-fill-mode: forwards;
    }

    .telegram-block:hover {
        box-shadow: 0px 5px 49px 36px rgba(14, 25, 34, 0.3) inset;
    }

    .vk-group-block {
        background-color: rgb(126, 189, 251);
        opacity: 0;


        animation: vk-group-show 1s 1;
        animation-fill-mode: forwards;
    }

    .youtube-block {
        background-color: rgb(251, 126, 126);
        opacity: 0;


        animation: youtube-show 1s 1;
        animation-fill-mode: forwards;
    }

    .rutube-block {
        background-color: rgb(60, 80, 131);
        opacity: 0;


        animation: rutube-show 1s 1;
        animation-fill-mode: forwards;
    }

    .telegram-bot-block {
        background-color: rgb(186, 187, 190);
        opacity: 0;

        animation: telegram-bot-show 1s 1;
        animation-fill-mode: forwards;
    }

    .nav-tip {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .nav-tip-title {
        opacity: 0;
        animation: nav-title-show 1s 0.4s 1;
        animation-fill-mode: forwards;
    }

    .nav-tip-arrow {
        opacity: 0;
        transform: translateY(10px);
        animation: nav-arrow-show 2s 0.6s infinite;
    }

    @media (min-height: 1000px) {
        .link-block {
            height: 180px;
            width: 180px;
        }

        .telegram-block {
            height: 180px;
            width: 380px;
        }

    }

    @media (max-height: 700px) {
        .link-block {
            height: 90px;
            width: 90px;
            font-size: 30px;
        }

        .resources-block {
            display: flex;
            gap: 10px;
        }

        .telegram-block {
            height: 90px;
            width: 190px;
        }

        .flex-double-block {
            gap: 10px;
        }

        .nav-tip {
            display: none;
        }
    }

</style>