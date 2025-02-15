import axios from 'axios';

import { IDate, IDateAdd, IDateUpdate } from '../interfaces/DateInterface';
import { apiUrl } from '../lib/axios';

export const dateApi = {
    async getDates() {
        return await axios.get<IDate[]>(`${apiUrl}/dates/all`);
    },

    async addDate(item: IDateAdd) {
        await axios.post(`${apiUrl}/dates`, item);
    },

    async updateDate(item: IDateUpdate) {
        await axios.patch(`${apiUrl}/dates`, item);
    },

    async deleteDate(itemId: number) {
        await axios.delete(`${apiUrl}/dates/${itemId}`);
    },
};
