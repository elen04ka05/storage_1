const versions = [
  {
    date: 'December 23, 2023, 10:48',
    code: 'import requests\nimport uvicorn\nimport random\nfrom fastapi import FastAPI, HTTPException\n\napp = FastAPI()',
  },
  {
    date: 'December 12, 2023, 16:23',
    code: 'import requests\nimport uvicorn\nimport random\nfrom fastapi import FastAPI, HTTPException\n\napp = FastAPI()',
  },
  {
    date: 'December 01, 2023, 18:12',
    code: 'import requests\nimport uvicorn\nimport random\nfrom fastapi import FastAPI, HTTPException\n\napp = FastAPI()',
  },
  {
    date: 'November 25, 2023, 19:17',
    code: 'import requests\nimport uvicorn\nimport random\nfrom fastapi import FastAPI, HTTPException\n\napp = FastAPI()',
  },
  {
    date: 'September 12, 2023, 14:23',
    code: 'import requests\nimport uvicorn\nimport random\nfrom fastapi import FastAPI\n\napp = FastAPI()',
  },
]

const returnButton = document.getElementById('return-button')
const restoreButton = document.getElementById('restore-button')
const versionsContainer = document.getElementById('versions-container')
const codeElement = document.getElementById('code')

returnButton.addEventListener('click', () => {
    window.location.href = '/snippet'
})

let historyButtons = []

const createHistoryButton = (date, code, isActive) => {
console.log('isActive: ', isActive);
console.log('date: ', date);
  const div = document.createElement('div')
  div.className = 'pt-4 px-4 cursor-pointer hover:bg-slate-200 active:bg-slate-100 pb-12 font-bold'
  div.classList.add(isActive ? 'bg-slate-200' : 'bg-slate-100')
  div.textContent = date

  div.addEventListener('click', () => {
    codeElement.textContent = code
    historyButtons.forEach(button => {
      button.classList.remove('bg-slate-200')
      button.classList.add('bg-slate-100')
    })
    div.classList.add('bg-slate-200')
  })

  return div
}

historyButtons = versions.map(({ date, code }, index) => {
  return createHistoryButton(date, code, index === 0)
})

historyButtons.forEach(element => {
  versionsContainer.appendChild(element)
})
