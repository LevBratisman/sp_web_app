<template>
    <div class="calendar-date-wrapper">    
        <div v-if="!isEvent">
            <span class="calendar-date" v-if="props.date != d.getDate() || props.month != d.getMonth() || props.year != d.getFullYear()">{{ props.date }}</span>
            <span v-else-if="theme.global.name.value === 'light'" class="calendar-date calendar-date-today">{{ props.date }}</span>
            <span v-else class="calendar-date calendar-date-today-dark">{{ props.date }}</span>
        </div>
        <div v-else>
            <span :class="`calendar-date ${getEventStyleClass}`" v-if="props.date != d.getDate() || props.month != d.getMonth() || props.year != d.getFullYear()">{{ props.date }}</span>
            <span v-else-if="theme.global.name.value === 'light'" :class="`calendar-date calendar-date-today ${getEventStyleClass}`">{{ props.date }}</span>
            <span v-else :class="`calendar-date calendar-date-today-dark ${getEventStyleClass}`">{{ props.date }}</span>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { onMounted, onUpdated, ref, computed } from 'vue';
    import { useTheme } from 'vuetify';

    import { IDate } from '../../interfaces/DateInterface'; 

    const props = defineProps<{
        date: number | null
        month: number
        year: number
        events: IDate[]
    }>();

    const theme = useTheme();

    const isEvent = ref(false);
    const curEvent = ref<IDate | null>(null);

    const getEventStyleClass = computed(() => {
    if (!curEvent.value) return '';
    switch (curEvent.value.typeOfEvent) {
        case 'BIRTHDAY':
            return 'calendar-date-birthday';
        case 'DISCOVERY':
            return 'calendar-date-discovery';
        case 'AWARD':
            return 'calendar-date-award';
    }
})

    const d = new Date();

    onUpdated(() => {
        if (props.date && props.events) {
            const fullDate = new Date(props.year, props.month, props.date);
            for (const event of props.events) {
                if (new Date(event.eventDate).getMonth() === fullDate.getMonth() && new Date(event.eventDate).getDate() === fullDate.getDate()) {
                    curEvent.value = event;
                    isEvent.value = true;
                    break;
                }
            }
        }
    })

</script>

<style scoped>

    .calendar-date-wrapper {
        font-weight: 900;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .calendar-date {
        width: 50px;
        height: 50px;
        font-size: 24px;
        border-radius: 50%;
        font-style: bold;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    @media (max-width: 1000px) {
        .calendar-date {
            width: 40px;
            height: 40px;
            font-size: 20px;
        }
    }

    @media (max-width: 480px) {
        .calendar-date {
            width: 30px;
            height: 30px;
            font-size: 20px;
        }
    }

    .calendar-date-today {    
        box-shadow: 0 0 2px 2px #000000 inset;
        font-weight: bold;
        border-radius: 50%;
        font-style: bold;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .calendar-date-today-dark {
        box-shadow: 0 0 2px 2px #ffffff inset;
        font-weight: bold;
        border-radius: 50%;
        font-style: bold;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .calendar-date-birthday {
        background-color: #5b7fff;
        color: white;
        font-weight: bold;
        border-radius: 50%;
        font-style: bold;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .calendar-date-discovery {
        background-color: #5b7fff;
        color: white;
        font-weight: bold;
        border-radius: 50%;
        font-style: bold;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .calendar-date-award {
        background-color: #5b7fff;
        color: white;
        font-weight: bold;
        border-radius: 50%;
        font-style: bold;
        display: flex;
        justify-content: center;
        align-items: center;
    }

</style>
