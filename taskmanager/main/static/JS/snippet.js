const returnButton = document.getElementById('return-button')
const copyButton = document.getElementById('copy-button')
const header = document.getElementById('header')
const codeContainer = document.getElementById('code-container')
const editButton = document.getElementById('edit-button')
const deleteButton = document.getElementById('delete-button')
const historyButton = document.getElementById('history-button')
const debugButton = document.getElementById('debug-button')

const getCode = () => {
    const content = codeContainer.textContent
    return content.split('\n').map(line => line.trim()).join('\n').trim()
}

returnButton.addEventListener('click', () => {
    window.location.href = '/home'
})

copyButton.addEventListener('click', async () => {
    const code = getCode()
    try {
        await navigator.clipboard.writeText(code)
    } catch (err) {
        console.error('Failed to copy: ', err)
    }
})

editButton.addEventListener('click', () => {
    const saveButton = document.createElement('button')
    saveButton.textContent = 'Save'
    saveButton.className = 'rounded-full bg-slate-100 py-1 px-4 cursor-pointer hover:bg-slate-200 active:bg-slate-100'
    editButton.replaceWith(saveButton)

    const cancelButton = document.createElement('button')
    cancelButton.textContent = 'Cancel'
    cancelButton.className = 'rounded-full bg-slate-100 py-1 px-4 cursor-pointer hover:bg-slate-200 active:bg-slate-100'
    deleteButton.replaceWith(cancelButton)

    const input = document.createElement('input')
    input.value = header.textContent.trim()
    input.className = "h-9 w-96"
    header.replaceWith(input)

    const textArea = document.createElement('textarea')
    textArea.className = 'm-4 p-4 h-80 box-border'
    textArea.style.width = 'calc(100% - 32px)'
    textArea.value = getCode()
    codeContainer.replaceWith(textArea)

    saveButton.addEventListener('click', () => {
        saveButton.replaceWith(editButton)
        cancelButton.replaceWith(deleteButton)
        input.replaceWith(header)
        textArea.replaceWith(codeContainer)
    })

    cancelButton.addEventListener('click', () => {
        saveButton.replaceWith(editButton)
        cancelButton.replaceWith(deleteButton)
        input.replaceWith(header)
        textArea.replaceWith(codeContainer)
    })
})

deleteButton.addEventListener('click', () => {

})

historyButton.addEventListener('click', () => {

})

debugButton.addEventListener('click', () => {

})
