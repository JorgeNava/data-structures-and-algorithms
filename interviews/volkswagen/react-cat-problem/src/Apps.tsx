import { useState, useEffect } from "react";

const CAT_ENDPOINT_RANDOM_FACT = 'https://catfact.ninja/fact'

export function App() {
  const [fact, setFact] = useState('lorem ipsum cat fact whatever');
  const [factFetched, setFactFetched] = useState(false);
  const [imageUrl, setImageUrl] = useState('');

  useEffect(() => {
    fetchData()
  }, []);

  useEffect(() => {
    if (factFetched) fetchImage()
  }, [factFetched]);

  const fetchData = async () => {
    try {
      const response = await fetch(CAT_ENDPOINT_RANDOM_FACT);
      const json = await response.json();
      const { fact } = json;
      setFact(fact);
      setFactFetched(true)

    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  const fetchImage = async () => {
    try {
      const firstWord = fact.split(' ')[0];
      const CAT_ENDPOINT_IMAGE_URL = `https://cataas.com/cat/says/${firstWord}?size=50&color=red&json=true`
      const response = await fetch(CAT_ENDPOINT_IMAGE_URL);
      const json = await response.json();
      setImageUrl(`https://cataas.com/${json.url}`);
    } catch (error) {
      console.error('Error fetching image:', error);
    }
  };

  return (
    <main style={{display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', width: '100vw', height: '100vh'}}>
      <h1>App de gatitos</h1>
      <p>{fact}</p>
      <img src={imageUrl} alt='Recovering cat image' style={{width: '500px'}}/>
    </main>
  )
}