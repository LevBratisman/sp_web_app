<template>
    <div class="pa-4 text-center">
        <v-dialog
        v-model="props.dialog"
        max-width="600"
        >
            <v-card
                prepend-icon="mdi-account"
                title="Изменить участника"
            >
                <v-card-text>

                    <v-sheet class="mx-auto">
                        <v-form v-model="form" fast-fail @submit.prevent>

                            <v-text-field
                                v-model="memberUpdateForm.name"
                                :rules="fieldRules"
                                label="Имя"
                                required
                            ></v-text-field>

                            <v-select
                                v-model="memberUpdateForm.role"
                                clearable
                                :rules="fieldRules"
                                label="Роль"
                                :items="roles"
                                required
                            ></v-select>

                            <v-select
                                v-model="memberUpdateForm.classYear"
                                clearable
                                label="Курс"
                                :items="classes"
                            ></v-select>

                            <v-select
                                v-model="memberUpdateForm.faculty"
                                clearable
                                label="Факультет"
                                :items="faculties"
                            ></v-select>

                            <v-text-field
                                v-model="memberUpdateForm.major"
                                label="Направление"
                            ></v-text-field>

                            <v-text-field
                                v-model="memberUpdateForm.majorCode"
                                label="Код направления"
                            ></v-text-field>

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
                                    @click="updateMember"
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

    import { IMember, IMemberUpdate } from '../../interfaces/MemberInterface';
    import { useBaseStore } from '../../store/modules/base';
    import { fieldRules, imageRules } from '../../utils/rules';

    const baseStore = useBaseStore();

    const props = defineProps<{
        dialog: Boolean,
        member: IMember
    }>()

    const emit = defineEmits(['closeDialog']);

    const memberUpdateForm = ref<IMemberUpdate>({
        id: props.member.id,
        name: props.member.name,
        role: props.member.role,
        imageId: props.member.imageId,
        classYear: props.member.classYear,
        faculty: props.member.faculty,
        major: props.member.major,
        majorCode: props.member.majorCode
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

    const imageFile = ref();
    const form = ref(false);

    const updateMember = async () => {
        if (!form.value) return;

        if (imageFile.value) {
            const uuidImage = uuidv4();

            const xhr = new XMLHttpRequest();
            const formData = new FormData();

            formData.append('image', imageFile.value, uuidImage);

            xhr.open('POST', 'https://simplephysics.ru/api/members/upload/image')
            xhr.send(formData);

            memberUpdateForm.value.imageId = uuidImage;
        }
        
        const error = await baseStore.updateMember(memberUpdateForm.value);

        if (error) {
            return;
        }
        
        emit('closeDialog');
    }

</script>

<style scoped>

</style>