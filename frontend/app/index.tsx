import { ScrollView } from 'react-native';
import Clickable from '@/components/Clickable';

const HomePage = () => {
  return (
    <ScrollView>
      <Clickable title="StationA" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']} onPress={() => alert('Button pressed!')}/>
      <Clickable title="StationB" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']} onPress={() => alert('Button pressed!')}/>
      <Clickable title="StationC" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']} onPress={() => alert('Button pressed!')}/>
      <Clickable title="StationD" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']} onPress={() => alert('Button pressed!')}/>
      <Clickable title="StationD" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']} onPress={() => alert('Button pressed!')}/>
      <Clickable title="StationD" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']} onPress={() => alert('Button pressed!')}/>
      <Clickable title="StationD" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']} onPress={() => alert('Button pressed!')}/>
      <Clickable title="StationD" accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']} onPress={() => alert('Button pressed!')}/>
    </ScrollView>

  );
};

export default HomePage;