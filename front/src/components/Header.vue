<template>

    <v-app-bar elevation="8">
        
            <v-app-bar-title class="large-size">
                {{ title }}
            </v-app-bar-title>
            <v-app-bar-title class="phone-size">
                <img v-show="theme.global.name.value == 'light'" style="height: 100%; width: 120px; padding-top: 15px;" src="../../public/ava_dark.png"></img>
                <img v-show="theme.global.name.value == 'dark'" style="height: 100%; width: 120px; padding-top: 15px;" src="../../public/ava_light.png"></img>
            </v-app-bar-title>
        
        <v-spacer></v-spacer>

        <div class="theme-switcher-block">
            <v-btn v-show="theme.global.name.value=='light'" :ripple="false" class="theme-switcher" @click="toggleTheme" icon="mdi-weather-sunny"></v-btn>
            <v-btn v-show="theme.global.name.value=='dark'" :ripple="false" class="theme-switcher" @click="toggleTheme" icon="mdi-weather-night"></v-btn>
        </div>

    </v-app-bar>

</template>

<script setup>
    import { defineProps } from 'vue';
    import { useTheme } from 'vuetify';
    
    import { useBaseStore } from '../store/modules/base'

    defineProps({
        title: String,
    });

    const baseStore = useBaseStore();

    const theme = useTheme();

    const toggleTheme = () => {
        baseStore.toggleTheme();
		theme.global.name.value = baseStore.theme;
    };
</script>

<style scoped>

    .theme-switcher-block {
        margin-right: 10px;
    }

    .main-link {
        text-decoration: none;
        transition: 0.3s;
    }

    .phone-size {
        display: none;
    }

    @media (max-width: 500px) {
        .phone-size {
            display: block;
        }
        .large-size {
            display: none;
        }
    }

</style>