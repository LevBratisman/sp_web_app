<template>
    <div class="calendar-block-wrapper">
        <p class="calendar-block-year" style="opacity: 0.5;">{{ curYear }}</p>

        <div class="calendar-block-months">
            <div class="calendar-block-month">
                <v-btn 
                    @click="prevMonth"
                    icon="mdi-menu-left"
                    variant="text"
                    :ripple="false"
                ></v-btn>
                <p style="width: 100px; text-align: center; font-weight: 900; font-size: 20px;">{{ months[curMonth].toUpperCase() }}</p>
                <v-btn 
                    @click="nextMonth"
                    icon="mdi-menu-right" 
                    variant="text"
                    :ripple="false"
                ></v-btn>
            </div>
        </div>
        <div class="calendar-block-info">
            <div class="calendar-block-days">
                <div :class="`calendar-block-day ${isHoliday(day)}`" v-for="day in daysOfWeek" :key="day">{{ day }}</div>
            </div>
            <div class="calendar-block-dates" v-auto-animate>
                <CalendarDate
                    v-if="monthDates.length > 0"
                    v-for="date in monthDates" :key="date.id"
                    :date="date.date" 
                    :month="curMonth" 
                    :year="curYear"
                    :events="events"
                ></CalendarDate>
            </div>
        </div>
    </div>
</template>

<script setup lang="ts">
    import { ref, onMounted, watch, onUpdated } from 'vue';
    import { storeToRefs } from 'pinia';
    import { useBaseStore } from '../../store/modules/base';

    import CalendarDate from './CalendarDate.vue';
    import { IDate } from '../../interfaces/DateInterface';

    const baseStore = useBaseStore();
    const { dates } = storeToRefs(baseStore);

    const emit = defineEmits(['monthChanged']);
    const props = defineProps<{
        events: IDate[]
    }>();

    const months = [
        'Январь',
        'Февраль',
        'Март',
        'Апрель',
        'Май',
        'Июнь',
        'Июль',
        'Август',
        'Сентябрь',
        'Октябрь',
        'Ноябрь',
        'Декабрь'
    ]
    const daysOfWeek = ['ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ', 'ВС'];

    const d = new Date();
    const curYear = ref(d.getFullYear());
    const curMonth = ref(d.getMonth());
    const curDay = ref(d.getDate());

    const isHoliday = (day: string) => {
        if (day === 'ВС' || day === 'СБ') {
            return 'calendar-block-holiday';
        }
    }
    
    const monthDates = ref([] as { date: number | null, id: string }[]);

    const prevMonth = () => {
        if (curMonth.value === 0) {
            curYear.value--;
            curMonth.value = 11;
        } else {
            curMonth.value--;
        }
        updateCalendar();
    }

    const nextMonth = () => {
        if (curMonth.value === 11) {
            curYear.value++;
            curMonth.value = 0;
        } else {
            curMonth.value++;
        }
        updateCalendar();
    }

    const updateCalendar = () => {
        const numberOfDays = new Date(curYear.value, curMonth.value + 1, 0).getDate();
        const startDayOfWeek = new Date(curYear.value, curMonth.value, 1).getDay();
        
        monthDates.value = [];
        
        // Заполнение пустых дат до начала месяца, чтобы соответствовать дням недели
        for (let i = 0; i < (startDayOfWeek === 0 ? 6 : startDayOfWeek - 1); i++) {
            monthDates.value.push({ date: null, id: `empty-${i}` });
        }
        
        for (let day = 1; day <= numberOfDays; day++) {
            monthDates.value.push({ date: day, id: `${curYear.value}-${curMonth.value}-${day}` });
        }

        // Заполнение пустых дат после конца месяца, чтобы соответствовать дням недели
        const totalSlots = 42;
        const remainingSlots = totalSlots - monthDates.value.length;
        for (let i = 0; i < remainingSlots; i++) {
            monthDates.value.push({ date: null, id: `post-empty-${i}` });
        }

        emit('monthChanged', curMonth.value);
    }

    onMounted(() => {
        updateCalendar();
    })
    watch([curYear, curMonth], updateCalendar);

</script>

<style scoped>
    .calendar-block-wrapper {
        width: 50vw;
        height: 500px;
        -webkit-box-shadow: 0px 0px 17px -4px rgba(34, 60, 80, 0.63);
        -moz-box-shadow: 0px 0px 17px -4px rgba(34, 60, 80, 0.63);
        box-shadow: 0px 0px 17px -4px rgba(34, 60, 80, 0.63);
        border-radius: 20px;
        padding: 20px;
    }

    @media (max-width: 1000px) {
        .calendar-block-wrapper {
            width: 70vw;
            height: 450px;
        }

        .calendar-block-days {
            gap: 0;
        }

        .calendar-block-dates {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            grid-template-rows: repeat(6, 1fr);
            gap: 0;
        }
    }

    @media (max-width: 700px) {
        .calendar-block-wrapper {
            width: 90vw;
            height: 420px;
        }        

        .calendar-block-year {
            display: none;
        }
    }

    @media (max-width: 480px) {
        .calendar-block-wrapper {
            width: 90vw;
            height: 350px;
        }

        .calendar-block-days {
            grid-template-columns: repeat(7, 35px) !important;
            justify-content: center;
        }

        .calendar-block-dates {
            grid-template-columns: repeat(7, 35px) !important;
            justify-content: center;
        }
    }

    .calendar-block-months {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 50px;
    }

    .calendar-block-month {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }

    .calendar-block-info {
        display: grid;
    }

    .calendar-block-days {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        gap: 5px;
        justify-items: center;
    }

    .calendar-block-day {
        width: 50px;
        height: 50px;
        font-weight: bold;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .calendar-block-dates {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        grid-template-rows: repeat(6, 1fr);
        gap: 5px;
        justify-items: center;
    }

    .calendar-block-date {
        width: 50px;
        height: 50px;
        border: 1px solid black;
        border-radius: 20px;
    }

    .calendar-block-holiday {
        color: #5b7fff;
    }

</style>
