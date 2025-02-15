<template>
    <div class="pa-4 text-center">
        <v-dialog
        v-model="props.dialog"
        max-width="600"
        >
            <v-card
                prepend-icon="mdi-post"
                title="Изменить пост"
            >
                <v-card-text>

                    <v-sheet class="mx-auto">
                        <v-form v-model="form" fast-fail @submit.prevent>

                            <v-text-field
                                v-model="postUpdateForm.title"
                                label="Заголовок"
                            ></v-text-field>

                            <v-textarea
                                v-model="postUpdateForm.description"
                                clear-icon="mdi-close-circle"
                                :rules="fieldRules"
                                label="Текст"
                                clearable
                            ></v-textarea>

                            <v-file-input
                                v-model="imageFile"
                                clearable
                                accept="image/png, image/jpeg, image/bmp, image/jpg"
                                label="Картинка"
                            ></v-file-input>

                            <v-divider></v-divider>

                            <v-card-actions style="display: block; text-align: right; padding-top: 20px;">
                                <v-btn
                                    text="Закрыть"
                                    variant="plain"
                                    @click="$emit('closeDialog')"
                                ></v-btn>

                                <v-btn
                                    type="submit"
                                    color="primary"
                                    variant="tonal"
                                    text="Изменить"
                                    @click="updatePost"
                                ></v-btn>
                            </v-card-actions>
                            
                        </v-form>
                    </v-sheet>

                </v-card-text>
            </v-card>
        </v-dialog>
    </div>
</template>

<script setup lang="ts">
    import { onUpdated, ref } from 'vue';
    import { v4 as uuidv4 } from 'uuid';

    import { IPost, IPostUpdate } from '../../interfaces/PostInterface';
    import { useBaseStore } from '../../store/modules/base';
    import { fieldRules } from '../../utils/rules';

    const baseStore = useBaseStore();

    const props = defineProps<{
        dialog: Boolean,
        post: IPost
    }>()

    const emit = defineEmits(['closeDialog']);

    const postUpdateForm = ref<IPostUpdate>({
        id: props.post.id,
        title: props.post.title,
        description: props.post.description,
        imageId: props.post.imageId,
    });

    const imageFile = ref();
    const form = ref(false);

    const updatePost = async () => {
        if (!form.value) return;

        if (imageFile.value) {
            const uuidImage = uuidv4();

            const xhr = new XMLHttpRequest();
            const formData = new FormData();

            formData.append('image', imageFile.value, uuidImage);

            xhr.open('POST', 'https://simplephysics.ru/api/posts/upload/image')
            xhr.send(formData);

            postUpdateForm.value.imageId = uuidImage;
        }
        
        const error = await baseStore.updatePost(postUpdateForm.value);

        if (error) {
            return;
        }
        
        emit('closeDialog');
    }

</script>

<style scoped>

</style>