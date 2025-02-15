import axios from 'axios';

import { IMember, IMemberAdd, IMemberUpdate } from '../interfaces/MemberInterface';
import { apiUrl } from '../lib/axios';

export const memberApi = {
    async getMembers() {
        return await axios.get<IMember[]>(`${apiUrl}/members/all`);
    },

    async addMember(item: IMemberAdd) {
        await axios.post(`${apiUrl}/members`, item);
    },

    async updateMember(item: IMemberUpdate) {
        await axios.patch(`${apiUrl}/members`, item);
    },

    async deleteMember(itemId: number) {
        await axios.delete(`${apiUrl}/members/${itemId}`);
    },

    async getMemberImage(uuid: string) {
        const response = await axios.get(`${apiUrl}/members/get/image`, { params: {'uuid': uuid}, responseType: 'blob' });
        return response;
    },
};
