<template>
    <div class="admin-post-wrapper">

        <div class="add-post-btn">
            <v-btn color="green" @click="dialog = true" prepend-icon="mdi-plus">
                Добавить
            </v-btn>
        </div>
        
        <v-table fixed-header height="100vh">
            <thead>
                <tr>
                    <th 
                    v-for="col in columns" 
                    :key="col.field"
                    style="text-align: center;"
                    >
                    {{ col.label }}
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr
                    v-for="post in posts"
                    :key="post.id"
                    align="center"
                >
                    <td>{{ post.id }}</td>
                    <td>{{ post.title }}</td>
                    <td style="max-width: 200px;">{{ post.description }}</td>
                    <td>{{ post.createdAt }}</td>
                    <td>
                        <div class="action-btns" style="text-align: center;">
                            <v-btn
                                variant="text"
                                color="primary"
                                icon="mdi-pencil"
                                @click="editPost(post)"
                            />
                            <v-btn
                                variant="text"
                                color="red"
                                icon="mdi-delete"
                                @click="deletePost(post.id)"
                            />
                        </div>
                    </td>
                </tr>
            </tbody>
        </v-table>
        <AddPostForm v-if="dialog" :dialog="dialog" @close-dialog="closeDialog"></AddPostForm>
        <EditPostFrom v-if="editDialog" :dialog="editDialog" :post="editingPost" @close-dialog="closeDialog"></EditPostFrom>
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue';
    import { storeToRefs } from 'pinia';
    import { onMounted } from 'vue';

    import { useBaseStore } from '../../store/modules/base';
    import AddPostForm from '../../components/admin/AddPostForm.vue';
    import EditPostFrom from '../../components/admin/EditPostFrom.vue';
    import { IPost } from '../../interfaces/PostInterface';
    import router from '../../router/index';


    const baseStore = useBaseStore();
    const { posts, adminAccessToken } = storeToRefs(baseStore);
    const dialog = ref(false);
    const editDialog = ref(false);

    const editingPost = ref<IPost>();

    const columns = [
        {
            name: 'id',
            label: 'Номер',
            field: 'id',
        },
        {
            name: 'title',
            label: 'Название',
            field: 'title',
        },
        {
            name: 'description',
            label: 'Описание',
            field: 'description',
        },
        {
            name: 'createdAt',
            label: 'Создано',
            field: 'createdAt',
        },
        {
            name: 'action',
            label: 'Действие',
            field: 'action',
        },
    ];

    const closeDialog = () => {
        dialog.value = false;
        editDialog.value = false;
    }

    const deletePost = async (postId: number) => {
        await baseStore.deletePost(postId);
    }

    const editPost = (post: IPost) => {
        editingPost.value = post;
        editDialog.value = true;
    }

    onMounted(async() => {
        baseStore.getAdminAccessToken();

        if (!adminAccessToken.value) {
            router.push({ name: 'Admin-login' });
        }

        await baseStore.getPosts();
    })

</script>

<style scoped>

    .admin-post-wrapper {
        padding: 10px;
    }

</style>