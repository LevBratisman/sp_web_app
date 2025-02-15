<template>
    <div id="start"></div>
    
    <v-container class="bg-image">
        
        <div class="introduce__content">
            <h1 style="margin-bottom: 15px;">
            SIMPLE PHYSICS
            </h1>
            <p style="margin-bottom: 15px;">
            «Simple physics» - это студенческий инициативный проект Московского политехнического университета, созданный для того,
            чтобы сделать изучение физики доступным и увлекательным для всех.
            Мы верим, что <router-link :to="{ name: 'Admin-login' }">ф</router-link>изика — это не только сложные формулы и абстрактные теории, и каждой публикацией мы стремимся это доказать! 
            </p>
            <p style="margin-bottom: 15px;">
            Хотите себя развлечь, но с пользой? Тогда открывайте наши тематические комиксы! 
            Готовитесь к зачёту по кинематике, динамике или ещё какой-то теме? 
            Для вас – лаконичные конспекты, в которых собрано всё, что нужно. Любите юмор?
            Даже тут мы подсуетились и нашли не только смешные, но и полезные мемы! 
            Шортсы, интересные факты из мира науки, да ещё и в красивом оформлении, разборы фильмов с точки зрения физики и многое другое – всё это у нас есть! 
            </p>
            <p style="margin-bottom: 15px;">
            Мы стремимся сделать науку доступной для каждого. Присоединяйтесь к нам и откройте для себя увлекательный мир физики!
            </p>
        </div>
    
    </v-container>
</template>

<script setup lang="ts">

    import { useTheme } from 'vuetify';

    const theme = useTheme();

</script>

<style scoped>

    a {
        text-decoration: none;
        color: inherit;
    }

    @keyframes appear{
        0%{
            opacity:0;
        }
        100% {
            opacity:1;
            transform: scale(1);
        }
    }

    .bg-image {
        height: calc(100vh - 120px);
        min-width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        position: relative;
    }

    .introduce__content {
        opacity: 0;
        text-align: center;
        padding: 50px 65px;
        max-width: 600px;

        transform: scale(0.8);
        animation: appear 1s 1;
        animation-fill-mode: forwards;
    }

    @media (max-width: 601px) {
        .introduce__content {
            padding: 20px 20px;
            font-size: 12px;
        }

        .content-title {
            margin-bottom: 10px;
        }
    }


    @media (min-height: 890px) {
        .introduce__content {
            font-size: 16px;
        }
    }

    @media (min-height: 1000px) {
        .introduce__content {
            font-size: 20px;
        }
        .content-title {
            margin-bottom: 25px;
        }
    }

    @media (max-height: 600px) {
        .introduce__content {
            padding: 20px 20px;
            font-size: 10px;
        }
    }

</style>
