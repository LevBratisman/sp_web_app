import { IPost } from "../interfaces/PostInterface";
import { IMember } from "../interfaces/MemberInterface";
import { IDate } from "../interfaces/DateInterface";

export interface BaseState {
    posts: IPost[] | null;
    members: IMember[] | null;
    dates: IDate[] | null;
    theme: string;
    adminAccessToken: Boolean;
}