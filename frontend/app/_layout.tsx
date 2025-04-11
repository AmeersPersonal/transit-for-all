import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import HomeScreen from './index';
import StationDetails from './info';

const Stack = createNativeStackNavigator();

export default function RootLayout() {
  return (
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="StationDetails" component={StationDetails} />
      </Stack.Navigator>
  );
}
