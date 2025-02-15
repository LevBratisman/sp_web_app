export const fieldRules = [
    value => {
        if (value) return true

        return 'Field is requred.'
    }
]

export const imageRules = [
    value => {
        if (value) return true

        return 'Image is requred.'
    }
]