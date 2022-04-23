import React from 'react'


const PageFooter = () => {
    return (
        <div>
            <h3>"Подвал" сайта</h3>
            <br></br>
            <ul>
                <li key={'FAQ'}>
                    <h5>Частые вопросы</h5>
                </li>
                <li key={'search'}>
                    <h5>Поиск</h5>
                </li>
                <li key={'callback'}>
                    <h5>Обратная связь</h5>
                </li>
            </ul>
        </div>
    )
}

export default PageFooter;