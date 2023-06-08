import { createRoot } from 'react-dom/client'
import { App } from './Apps.tsx';

const root = createRoot(document.getElementById('app'))
root.render(<App />)