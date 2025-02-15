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
                    v-for="member in members"
                    :key="member.id"
                    align="center"
                >
                    <td>{{ member.id }}</td>
                    <td>{{ member.name }}</td>
                    <td>{{ member.role }}</td>
                    <td>{{ member.classYear }}</td>
                    <td>
                        <div class="action-btns" style="text-align: center;">
                            <v-btn
                                variant="text"
                                color="primary"
                                icon="mdi-pencil"
                                @click="editMember(member)"
                            />
                            <v-btn
                                variant="text"
                                color="red"
                                icon="mdi-delete"
                                @click="deleteMember(member.id)"
                            />
                        </div>
                    </td>
                </tr>
            </tbody>
        </v-table>
        <AddMemberForm v-if="dialog" :dialog="dialog" @close-dialog="closeDialog"></AddMemberForm>
        <EditMemberForm v-if="editDialog" :dialog="editDialog" :member="editingMember" @close-dialog="closeDialog"></EditMemberForm>
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue';
    import { storeToRefs } from 'pinia';
    import { onMounted } from 'vue';

    import { useBaseStore } from '../../store/modules/base';
    import AddMemberForm from '../../components/admin/AddMemberForm.vue';
    import EditMemberForm from '../../components/admin/EditMemberForm.vue';
    import { IMember } from '../../interfaces/MemberInterface';
    import router from '../../router/index';


    const baseStore = useBaseStore();
    const { members, adminAccessToken } = storeToRefs(baseStore);
    const dialog = ref(false);
    const editDialog = ref(false);

    const editingMember = ref<IMember>();

    const columns = [
        {
            name: 'id',
            label: 'Номер',
            field: 'id',
        },
        {
            name: 'name',
            label: 'Имя',
            field: 'name',
        },
        {
            name: 'role',
            label: 'Роль',
            field: 'role',
        },
        {
            name: 'classYear',
            label: 'Курс',
            field: 'classYear',
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

    const deleteMember = async (memberId: number) => {
        await baseStore.deleteMember(memberId);
    }

    const editMember = (member: IMember) => {
        editingMember.value = member;
        editDialog.value = true;
    }

    onMounted(async() => {
        baseStore.getAdminAccessToken();

        if (!adminAccessToken.value) {
            router.push({ name: 'Admin-login' });
        }

        await baseStore.getMembers();
    })

</script>

<style scoped>

    .admin-member-wrapper {
        padding: 10px;
    }

</style>