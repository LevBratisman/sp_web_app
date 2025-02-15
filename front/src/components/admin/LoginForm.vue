<template>
    <div class="admin-login-form-wrapper">
        <v-sheet class="mx-auto" width="300">
            <v-form v-model="form" fast-fail @submit.prevent="submitForm">
                <v-text-field
                    v-model="login"
                    :rules="fieldRules"
                    label="Login"
                ></v-text-field>

                <v-text-field
                    v-model="password"
                    :rules="fieldRules"
                    label="Password"
                    type="password"
                ></v-text-field>

                <v-btn color="primary" class="mt-2" type="submit" block>Sign in</v-btn>
            </v-form>
        </v-sheet>
    </div>
</template>

<script setup lang="ts">
    import { ref } from 'vue';

    import { fieldRules } from '../../utils/rules';
    import { useBaseStore } from '../../store/modules/base';
    import router from '../../router/index';

    const baseStore = useBaseStore();

    const login = ref('');
    const password = ref('');

    const form = ref(false);

    const submitForm = () => {
        if (!form.value) return;

        if (login.value == 'admin' && password.value == 'admin321') {
            baseStore.setAdminAccessToken();
            router.push({name: 'Admin-panel'});
        }
    }

</script>

<style scoped>

</style>