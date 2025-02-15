<template>
    <div class="calendar-panel-wrapper" v-auto-animate>
        <PanelInfoBlock :event="event" v-for="event in props.events" :key="event.id"></PanelInfoBlock>
    </div>
</template>

<script setup lang="ts">

    import { IDate } from '../../interfaces/DateInterface';
    import PanelInfoBlock from './PanelInfoBlock.vue';

    const props = defineProps<{
        events: IDate[]
    }>();

</script>

<style scoped>
    .calendar-panel-wrapper {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        gap: 20px;
        padding: 40px;
        width: 30vw;
        max-height: 100vh;
        overflow: scroll;
        height: inherit;
    }

    @media screen and (max-width: 1000px) {
        .calendar-panel-wrapper {
            width: 100vw;
            align-items: flex-start;
        }
    }
</style>
