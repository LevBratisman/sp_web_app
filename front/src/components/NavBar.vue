<template>
    <v-layout class="overflow-visible" style="height: 56px;">
        <v-bottom-navigation
          style="position: fixed;"
          class="navbar"
          v-model="navbar"
          color="teal"
          grow
        >
            <v-btn to="/about" :ripple="false">
                <v-icon>mdi-home</v-icon>
                <span class="nav-btn-text">О проекте</span>
            </v-btn>

            <v-btn to="/resources" :ripple="false">
                <v-icon>mdi-atom</v-icon>
                <span class="nav-btn-text">Ресурсы</span>
            </v-btn>
      
            <v-btn to="/team" :ripple="false">
                <v-icon>mdi-account-group-outline</v-icon>
                <span class="nav-btn-text">Команда</span>
            </v-btn>

            <v-btn to="/calendar" :ripple="false">
                <v-icon>mdi-calendar</v-icon>
                <span class="nav-btn-text">Календарь</span>
            </v-btn>
      
            <v-btn to="/news" :ripple="false">
                <v-icon>mdi-new-box</v-icon>
                <span class="nav-btn-text">Новости</span>
            </v-btn>
        </v-bottom-navigation>
        <v-main>
            <router-view></router-view>
        </v-main>
    </v-layout>
</template>

<script setup>
    import { ref } from 'vue';

    const navbar = ref(1);
</script>

<style scoped>

    @media screen and (max-width: 600px) {
        .nav-btn-text {
            display: none !important
        }
    }

</style>