<template>
    <div class="admin-layout-wrapper">
        <div class="admin-layout-navbar">
            <Navbar></Navbar>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { onMounted } from 'vue';
    import { storeToRefs } from 'pinia';

    import { useBaseStore } from '../store/modules/base';
    import Navbar from '../components/admin/Navbar.vue';
    import router from '../router/index';


    const baseStore = useBaseStore();
    const { adminAccessToken } = storeToRefs(baseStore);


    onMounted(() => {
        baseStore.getAdminAccessToken();
        if (!adminAccessToken.value) {
            router.push({ name: 'Admin-login' });
        }
    })
</script>

<style scoped>

</style>