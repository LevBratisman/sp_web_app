<template>
    <div class="calendar-panel-block-wrapper">
        <div class="calendar-panel-block-date">{{ getConvertedDate(event.eventDate) }}</div>
        <div class="calendar-panel-block-info">
            <div :class="`calendar-panel-block-type calendar-panel-block-type-${event.typeOfEvent.toLowerCase()}`"></div>
            <span>{{ event.description }}</span>
        </div>
    </div>
</template>

<script setup lang="ts">

    import { IDate } from '../../interfaces/DateInterface';

    const props = defineProps<{
        event: IDate
    }>();

    const months = [
        'Января',
        'Февраля',
        'Марта',
        'Апреля',
        'Мая',
        'Июня',
        'Июля',
        'Августа',
        'Сентября',
        'Октября',
        'Ноября',
        'Декабря'
    ]

    const getConvertedDate = (date: string) => {
        const newDate = new Date(date);
        return `${newDate.getDate()} ${months[newDate.getMonth()]}, ${newDate.getFullYear()}г`
    }

</script>

<style scoped>

    .calendar-panel-block-wrapper {
        height: auto;
    }

    .calendar-panel-block-info {
        display: flex;
        gap: 10px;
        width: 100%;
        word-wrap: break-word;
    }

    .calendar-panel-block-type {
        min-width: 15px !important;
        height: 15px;
        border-radius: 50%;
        margin-top: 5px;
        margin-right: 10px;
    }

    .calendar-panel-block-date {
        opacity: 0.5;
        margin-left: 35px;
    }

    .calendar-panel-block-type-birthday {
        background-color: #5b7fff;
    }

    .calendar-panel-block-type-award {
        background-color: #5b7fff;
    }

    .calendar-panel-block-type-discovery {
        background-color: #5b7fff;
    }

    @media (max-width: 600px) {
        .calendar-panel-block-info {
            font-size: 14px;
        }
    }

</style>
