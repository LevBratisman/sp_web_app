<template>
    <v-card>
        <v-layout>
            <v-navigation-drawer
                theme="dark"
            >
                <v-list nav>
                    <v-list-item 
                        v-for="menuItem in menuList" 
                        :prepend-icon="menuItem.icon" 
                        :title="menuItem.title"
                        :to="{ name: menuItem.route }"
                    ></v-list-item>
                </v-list>

                <template v-slot:append>
                    <div class="pa-2">
                        <v-btn color="red" :to="{ name: 'Home' }" block>
                        Выйти
                        </v-btn>
                    </div>
                </template>
            </v-navigation-drawer>
            <v-main style="height: 100vh">
                <router-view></router-view>
            </v-main>
        </v-layout>
    </v-card>
</template>

<script setup lang="ts">

    import { ref } from 'vue';

    const menuList = [
        {
            icon: 'mdi-post',
            title: 'Посты',
            route: 'Posts',
        },
        {
            icon: 'mdi-human-greeting-variant',
            title: 'Участники',
            route: 'Members',
        },
        {
            icon: 'mdi-calendar',
            title: 'Даты',
            route: 'Dates',
        },
    ]

</script>

<style scoped>

</style>