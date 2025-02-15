export interface IDate {
    id: number;
    description: string;
    eventDate: string;
    typeOfEvent: string;
}

export interface IDateAdd {
    description: string | null;
    eventDate: string | null;
    typeOfEvent: string | null;
}

export interface IDateUpdate {
    id: number;
    description: string | null;
    eventDate: string | null;
    typeOfEvent: string | null;
}