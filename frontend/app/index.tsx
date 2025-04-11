import { ScrollView } from 'react-native';
import Clickable from '@/components/Clickable';

const HomePage = ({ navigation }) => {
  return (
    <ScrollView>
      <Clickable title="StationA" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']} onPress={() => navigation.navigate('StationDetails', { stationName: 'StationA' })}r/>
      <Clickable title="StationB" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']} onPress={() => alert('Button pressed!')}/>
    </ScrollView>

  );
};

export default HomePage;