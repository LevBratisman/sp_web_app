<template>
    <div class="calendar-wrapper">
        <div class="calendar-main-block">
            <CalendarBlock :events="events" @month-changed="getEventsByMonth"></CalendarBlock>
        </div>
        <CalendarPanel v-if="events.length > 0" :events="events" class="calendar-panel"></CalendarPanel>
    </div>
</template>

<script setup lang="ts">
    import { onMounted, ref } from 'vue';
    import { useBaseStore } from '../store/modules/base';
    import { storeToRefs } from 'pinia';

    import { IDate } from '../interfaces/DateInterface';
    import CalendarBlock from '../components/calendar/CalendarBlock.vue';
    import CalendarPanel from '../components/calendar/CalendarPanel.vue';

    const baseStore = useBaseStore();
    const { dates } = storeToRefs(baseStore);

    const events = ref<IDate[]>([]);

    onMounted(async () => {
        await baseStore.getDates().then(() => {
            getEventsByMonth(new Date().getMonth());
        })
    })

    const getEventsByMonth = (month: number) => {
        if (!dates.value) return;
        events.value = dates.value.filter((date: IDate) => {
            const eventDate = new Date(date.eventDate);
            return eventDate.getMonth() === month;
        });
}
</script>

<style scoped>
    .calendar-wrapper {
        display: flex;
        height: calc(100vh - 120px);
        justify-content: space-between;
    }

    @media screen and (max-width: 1000px) {
        .calendar-wrapper {
            padding-top: 50px;
            flex-direction: column;
        }
        .calendar-main-block {
            width: 100vw !important;
        }
    }

    @media screen and (max-width: 480px) {
        .calendar-wrapper {
            padding-top: 30px;
            flex-direction: column;
        }
    }

    .calendar-main-block {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 70vw;
    }

    .v-main {
        padding-top: 0 !important;
    }

</style>
