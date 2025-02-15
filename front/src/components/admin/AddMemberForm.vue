<template>
    <div class="pa-4 text-center">
        <v-dialog
        v-model="props.dialog"
        max-width="600"
        >
            <v-card
                prepend-icon="mdi-account"
                title="Добавить участника"
            >
                <v-card-text>

                    <v-sheet class="mx-auto">
                        <v-form ref="formRef" v-model="formIsValid" fast-fail @submit.prevent="addMember">

                            <v-text-field
                                v-model="memberAddForm.name"
                                :rules="fieldRules"
                                label="Имя"
                                required
                            ></v-text-field>

                            <v-select
                                v-model="memberAddForm.role"
                                clearable
                                :rules="fieldRules"
                                label="Роль"
                                :items="roles"
                                required
                            ></v-select>

                            <v-select
                                v-model="memberAddForm.classYear"
                                clearable
                                label="Курс"
                                :items="classes"
                            ></v-select>

                            <v-select
                                v-model="memberAddForm.faculty"
                                clearable
                                label="Факультет"
                                :items="faculties"
                            ></v-select>

                            <v-text-field
                                v-model="memberAddForm.major"
                                label="Направление"
                            ></v-text-field>

                            <v-text-field
                                v-model="memberAddForm.majorCode"
                                label="Код направления"
                            ></v-text-field>

                            <v-file-input
                                v-model="imageFile"
                                :rules="imageRules"
                                accept="image/png, image/jpeg, image/bmp, image/jpg"
                                label="Картинка"
                                required
                                clearable
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
                                    color="green"
                                    variant="tonal"
                                    text="Добавить"
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
    import { ref } from 'vue';
    import { v4 as uuidv4 } from 'uuid';

    import { IMemberAdd } from '../../interfaces/MemberInterface';
    import { useBaseStore } from '../../store/modules/base';
    import { fieldRules, imageRules } from '../../utils/rules';

    const baseStore = useBaseStore();

    const props = defineProps({
        dialog: Boolean,
    })

    const emit = defineEmits(['closeDialog']);

    const memberAddForm = ref<IMemberAdd>({
        name: null,
        role: null,
        imageId: null,
        classYear: null,
        faculty: null,
        major: null,
        majorCode: null
    });

    const roles = [
        'Участник',
        'Куратор',
        'Разработчик',
        'Дизайнер',
        'Писатель',
        'Контент-мейкер',
        'Монтажер',
        'Лидер команды'
    ]

    const classes = [
        '1 курс',
        '2 курс',
        '3 курс',
        '4 курс',
        'Магистр',
        'Аспирант',
        'Ассистент Центра проектной деятельности',
    ]

    const faculties = [
        'Инженерная школа',
        'Факультет довузовской подготовки',
        'Транспортный факультет',
        'Факультет информационных технологий',
        'Факультет химической технологии и биотехнологии',
        'Факультет экономики и управления',
        'Фестиваль рекламы «Лимон»',
        'Факультет машиностроения',
        'Факультет урбанистики и городского хозяйства',
        'Институт графики и искусства книги имени В.А.Фаворского',
        'Институт издательского дела и журналистики',
        'Полиграфический институт',
        'Факультет базовых компетенций',
        'Передовая инженерная школа электротранспорта'
    ]

    const imageFile = ref<File | null>(null);
    const formIsValid = ref(false);
    const formRef = ref(null);

    const addMember = async () => {
        if (!formRef.value || !formIsValid.value || !imageFile.value) return;

        if (imageFile.value) {
            const uuidImage = uuidv4();

            const xhr = new XMLHttpRequest();
            const formData = new FormData();

            formData.append('image', imageFile.value, uuidImage);

            xhr.open('POST', 'https://simplephysics.ru/api/members/upload/image')
            xhr.send(formData);

            memberAddForm.value.imageId = uuidImage;
        }
        
        const error = await baseStore.addMember(memberAddForm.value);

        if (error) {
            return;
        }

        memberAddForm.value = {
            name: null,
            role: null,
            imageId: null,
            classYear: null,
            faculty: null,
            major: null,
            majorCode: null
        }
        
        emit('closeDialog');
    }

</script>

<style scoped>

</style>