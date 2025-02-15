import axios from 'axios';

import { IPost, IPostAdd, IPostUpdate } from '../interfaces/PostInterface';
import { apiUrl } from '../lib/axios';

export const postApi = {
    async getPosts() {
        return await axios.get<IPost[]>(`${apiUrl}/posts/all`);
    },

    async addPost(item: IPostAdd) {
        await axios.post(`${apiUrl}/posts`, item);
    },

    async updatePost(item: IPostUpdate) {
        await axios.patch(`${apiUrl}/posts`, item);
    },

    async deletePost(itemId: number) {
        await axios.delete(`${apiUrl}/posts/${itemId}`);
    },

    async getPostImage(uuid: string | null) {
        const response = await axios.get(`${apiUrl}/posts/get/image`, { params: {'uuid': uuid}, responseType: 'blob' });
        return response;
    },

    async likePost(itemId: number) {
        await axios.patch(`${apiUrl}/posts/${itemId}/like`);
    },

    async dislikePost(itemId: number) {
        await axios.patch(`${apiUrl}/posts/${itemId}/dislike`);
    }
};
