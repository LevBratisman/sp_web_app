<template>
    <v-app>
        <v-main class="main-wrapper">
            <RouterView />  
        </v-main>
    </v-app>
</template>

<script setup lang="ts">
    import { RouterView } from 'vue-router'
</script>

<style>
    .v-timeline-item__body {
        max-width: 400px;
    }
</style>