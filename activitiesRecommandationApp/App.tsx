import React, {useEffect} from 'react';
import {SafeAreaView, StyleSheet} from 'react-native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

import {TamaguiProvider, createTamagui} from '@tamagui/core';
import {config} from '@tamagui/config';
import MainNavigation from './src/mainNavigation';

const tamaguiConfig = createTamagui(config);

// make TypeScript type everything based on your config
type Conf = typeof tamaguiConfig;
declare module '@tamagui/core' {
  interface TamaguiCustomConfig extends Conf {}
}

function App(): JSX.Element {
  // const [text, setText] = React.useState('');
  // const [tags, setTags] = React.useState([]);

  // const [timeoutId, setTimeoutId] = React.useState(null);

  // const onTextChange = (_text: string) => setText(_text);

  // useEffect(() => {
  //   if (timeoutId) {
  //     clearTimeout(timeoutId);
  //   }

  //   setTimeoutId(
  //     setTimeout(() => {
  //       fetch('http://10.0.2.2:5000/' + text)
  //         .then(response => response.json())
  //         .then(response => setTags(response))
  //         .catch(error => console.log(error));
  //     }, 2000),
  //   );
  // }, [text]);

  // const onSubmit = () => {
  //   fetch('http://10.0.2.2:5000/activity/' + text)
  //     .then(response => response.json())
  //     .then(response => setTags(response))
  //     .catch(error => console.log(error));
  // };

  return (
    <TamaguiProvider config={tamaguiConfig}>
      <MainNavigation />
    </TamaguiProvider>
  );
}

export default App;
