export interface IMember {
    id: number;
    name: string | null;
    role: string | null;
    imageId: string | null;
    classYear: string | null;
    faculty: string | null;
    major: string | null;
    majorCode: string | null;
}

export interface IMemberAdd {
    name: string | null;
    imageId: string | null;
    role: string | null;
    classYear: string | null;
    faculty: string | null;
    major: string | null;
    majorCode: string | null;
}

export interface IMemberUpdate extends IMember {}