import {useNavigation} from '@react-navigation/native';
import React, {useEffect, useState} from 'react';
import {Button, Form, H4, Input, Spinner} from 'tamagui';
const LoginScreen = () => {
  const navigation = useNavigation();
  const [user, setUser] = useState({username: '', password: ''});
  const [status, setStatus] = useState<'off' | 'submitting' | 'submitted'>(
    'off',
  );

  useEffect(() => {
    return () => {
      setStatus('off');
    };
  }, [status]);

  const fetchData = async () => {
    const response = await fetch('http://10.0.2.2:5000/login/', {
      method: 'POST',
      body: JSON.stringify(user),
    });
    const json = await response.json();
    console.log(json);
  };

  const handleSubmit = () => {
    fetchData()
      .then(() => {
        navigation.navigate('Home');
      })
      .catch(error => {
        console.error(error);
      });
    setStatus('submitted');
  };
  const handleTextChange = (label: string) => {
    return (value: string) =>
      setUser(prevState => ({...prevState, [label]: value}));
  };

  return (
    <Form
      alignItems="center"
      minWidth={300}
      gap="$2"
      onSubmit={() => setStatus('submitting')}
      borderWidth={1}
      borderRadius="$4"
      backgroundColor="$background"
      borderColor="$borderColor"
      padding="$8">
      <H4>{status[0].toUpperCase() + status.slice(1)}</H4>
      <Input
        value={user.username}
        onChangeText={handleTextChange('username')}
        backgroundColor="$background"
        placeholder="Username"
      />
      <Input
        value={user.password}
        onChangeText={handleTextChange('password')}
        backgroundColor="$background"
        placeholder="Password"
        secureTextEntry
      />
      <Form.Trigger asChild disabled={status !== 'off'}>
        <Button
          onPress={handleSubmit}
          icon={status === 'submitting' ? () => <Spinner /> : undefined}>
          Submit
        </Button>
      </Form.Trigger>
    </Form>
  );
};

export default LoginScreen;
