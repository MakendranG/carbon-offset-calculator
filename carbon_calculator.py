import json
from datetime import datetime

class CarbonFootprintCalculator:
    def __init__(self):
        self.ELECTRICITY_FACTOR = 0.233  # kg CO2 per kWh
        self.NATURAL_GAS_FACTOR = 0.185  # kg CO2 per kWh
        self.CAR_FACTOR = 0.404  # kg CO2 per mile
        self.FLIGHT_FACTOR = 0.255  # kg CO2 per mile
        
    def calculate_home_emissions(self, electricity_usage, natural_gas_usage):
        electricity_emissions = electricity_usage * self.ELECTRICITY_FACTOR
        gas_emissions = natural_gas_usage * self.NATURAL_GAS_FACTOR
        return electricity_emissions + gas_emissions
    
    def calculate_transport_emissions(self, car_miles, flight_miles):
        car_emissions = car_miles * self.CAR_FACTOR
        flight_emissions = flight_miles * self.FLIGHT_FACTOR
        return car_emissions + flight_emissions
    
    def get_offset_recommendations(self, total_emissions):
        recommendations = [
            {
                "action": "Plant trees",
                "impact": f"Plant {int(total_emissions/48)} trees to offset your annual emissions",
                "description": "One tree absorbs approximately 48 kg CO2 per year"
            },
            {
                "action": "Switch to renewable energy",
                "impact": "Reduce emissions by up to 70%",
                "description": "Install solar panels or switch to a renewable energy provider"
            },
            {
                "action": "Improve home insulation",
                "impact": "Reduce heating/cooling emissions by 15-20%",
                "description": "Update windows, doors, and wall insulation"
            },
            {
                "action": "Use public transport",
                "impact": "Reduce transport emissions by 30-60%",
                "description": "Replace car journeys with public transport where possible"
            }
        ]
        return recommendations

def main():
    calculator = CarbonFootprintCalculator()
    
    print("Carbon Footprint Calculator")
    print("==========================")
    
    electricity = float(input("Enter monthly electricity usage (kWh): "))
    natural_gas = float(input("Enter monthly natural gas usage (kWh): "))
    
    car_miles = float(input("Enter annual car mileage: "))
    flight_miles = float(input("Enter annual flight mileage: "))
    
    home_emissions = calculator.calculate_home_emissions(electricity, natural_gas)
    transport_emissions = calculator.calculate_transport_emissions(car_miles, flight_miles)
    total_emissions = home_emissions + transport_emissions
    
    print("\nYour Carbon Footprint Results")
    print("============================")
    print(f"Home Energy Emissions: {home_emissions:.2f} kg CO2/year")
    print(f"Transport Emissions: {transport_emissions:.2f} kg CO2/year")
    print(f"Total Carbon Footprint: {total_emissions:.2f} kg CO2/year")
    
    print("\nOffset Recommendations")
    print("====================")
    recommendations = calculator.get_offset_recommendations(total_emissions)
    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. {rec['action']}")
        print(f"Impact: {rec['impact']}")
        print(f"How: {rec['description']}")

if __name__ == "__main__":
    main()
