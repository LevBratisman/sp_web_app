<template>
    <div class="news-wrapper">
        <div v-if="posts?.length > 0" class="news-list" v-auto-animate>
            <PostCard v-for="post in posts" :post="post"></PostCard>
        </div>
        <div v-else class="lack-content" v-auto-animate>
            <h2>
                Нет новостей
            </h2>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { onMounted, ref } from 'vue';
    import { storeToRefs } from 'pinia';

    import { useBaseStore } from '../store/modules/base';
    import PostCard from '../components/PostCard.vue';

    const baseStore = useBaseStore();
    const { posts } = storeToRefs(baseStore);

    onMounted(async () => {
        await baseStore.getPosts();
    })

</script>

<style scoped>

    .news-list {
        display: flex;
        align-items: center;
        flex-direction: column;
        gap: 20px;
    }

    .news-wrapper {
        display: flex;
        align-items: center;
        justify-content: center;
        padding-bottom: 100px;
        padding-top: 50px;
        min-height: calc(100vh - 120px);
    } 

    .lack-content {
        opacity: 0.5;
    }

</style>