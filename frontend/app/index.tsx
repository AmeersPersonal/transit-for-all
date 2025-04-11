import { ScrollView } from 'react-native';
import Clickable from '@/components/Clickable';

const stations = ['59 St Columbus Circle', 'StationB', 'StationC', 'StationD'];

const HomePage = ({ navigation }) => {
  return (
    <ScrollView>
      {stations.map((station) => (
        <Clickable
          key={station}
          title={station}
          accessibilityDetails={['Elevators: Yes', 'Escalators: Yes']}
          onPress={() => navigation.navigate('StationDetails', { stationName: station })}
        />
      ))}
    </ScrollView>
  );
};

export default HomePage;