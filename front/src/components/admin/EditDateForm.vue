<template>
    <div class="pa-4 text-center">
        <v-dialog
        v-model="props.dialog"
        max-width="600"
        >
            <v-card
                prepend-icon="mdi-calendar"
                title="Изменить дату"
            >
                <v-card-text>

                    <v-sheet class="mx-auto">
                        <v-form v-model="form" fast-fail @submit.prevent>

                            <v-textarea
                                v-model="dateUpdateForm.description"
                                :rules="fieldRules"
                                label="Описание"
                                required
                            ></v-textarea>

                            <v-text-field
                                type="date"
                                v-model="dateUpdateForm.eventDate"
                                :rules="fieldRules"
                                label="Дата"
                                required
                            ></v-text-field>

                            <v-select
                                v-model="dateUpdateForm.typeOfEvent"
                                clearable
                                :rules="fieldRules"
                                label="Тип"
                                :items="eventTypes"
                            ></v-select>
                
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
                                    @click="updateDate"
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

    import { IDateUpdate, IDate } from '../../interfaces/DateInterface';
    import { useBaseStore } from '../../store/modules/base';
    import { fieldRules, imageRules } from '../../utils/rules';

    const baseStore = useBaseStore();

    const props = defineProps<{
        dialog: Boolean,
        date: IDate
    }>()

    const emit = defineEmits(['closeDialog']);

    const dateUpdateForm = ref<IDateUpdate>({
        id: props.date.id,
        description: props.date.description,
        eventDate: props.date.eventDate,
        typeOfEvent: props.date.typeOfEvent
    });

    const eventTypes = [
        'BIRTHDAY',
        'DISCOVERY',
        'AWARD'
    ]

    const form = ref(false);

    const updateDate = async () => {
        if (!form.value) return;

        const error = await baseStore.updateDate(dateUpdateForm.value);

        if (error) {
            return;
        }
        
        emit('closeDialog');
    }

</script>

<style scoped>

</style>