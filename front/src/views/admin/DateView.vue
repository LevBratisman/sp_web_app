<template>
    <div class="admin-member-wrapper">
        <div class="add-member-btn">
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
                    v-for="date in dates"
                    :key="date.id"
                    align="center"
                >
                    <td>{{ date.id }}</td>
                    <td style="max-width: 200px;">{{ date.description }}</td>
                    <td>{{ date.eventDate }}</td>
                    <td>{{ date.typeOfEvent }}</td>
                    <td>
                        <div class="action-btns" style="text-align: center;">
                            <v-btn
                                variant="text"
                                color="primary"
                                icon="mdi-pencil"
                                @click="editDate(date)"
                            />
                            <v-btn
                                variant="text"
                                color="red"
                                icon="mdi-delete"
                                @click="deleteDate(date.id)"
                            />
                        </div>
                    </td>
                </tr>
            </tbody>
        </v-table>
        <AddDateForm v-if="dialog" :dialog="dialog" @close-dialog="closeDialog"></AddDateForm>
        <EditDateForm v-if="editDialog" :dialog="editDialog" :date="editingDate" @close-dialog="closeDialog"></EditDateForm>
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue';
    import { storeToRefs } from 'pinia';
    import { onMounted } from 'vue';

    import { useBaseStore } from '../../store/modules/base';
    import AddDateForm from '../../components/admin/AddDateForm.vue';
    import EditDateForm from '../../components/admin/EditDateForm.vue';
    import { IDate } from '../../interfaces/DateInterface';
    import router from '../../router/index';


    const baseStore = useBaseStore();
    const { dates, adminAccessToken } = storeToRefs(baseStore);
    const dialog = ref(false);
    const editDialog = ref(false);

    const editingDate = ref<IDate>();

    const columns = [
        {
            name: 'id',
            label: 'Номер',
            field: 'id',
        },
        {
            name: 'description',
            label: 'Описание',
            field: 'description',
        },
        {
            name: 'eventDate',
            label: 'Дата',
            field: 'eventDate',
        },
        {
            name: 'typeOfEvent',
            label: 'Тип',
            field: 'typeOfEvent',
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

    const deleteDate = async (dateId: number) => {
        await baseStore.deleteDate(dateId);
    }

    const editDate = (date: IDate) => {
        editingDate.value = date;
        editDialog.value = true;
    }

    onMounted(async() => {
        baseStore.getAdminAccessToken();

        if (!adminAccessToken.value) {
            router.push({ name: 'Admin-login' });
        }

        await baseStore.getDates();
    })

</script>

<style scoped>

    .admin-member-wrapper {
        padding: 10px;
    }

</style>