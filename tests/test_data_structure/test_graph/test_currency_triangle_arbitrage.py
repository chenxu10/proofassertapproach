import pytest
import math
from collections import defaultdict

class CurrencyTriangleArbitrage:
    def __init__(self):
        pass
    
    def find_arbitrage(self, exchange_rates):
        """
        Find currency arbitrage opportunities using negative cycle detection.
        
        Args:
            exchange_rates: Dict of currency pairs to exchange rates
                           e.g., {('USD', 'EUR'): 0.85, ('EUR', 'GBP'): 0.90, ...}
        
        Returns:
            List of currencies forming arbitrage cycle, or empty list if none found
        """    
        graph = defaultdict(list)
        currencies = set()
        
        # Create graph
        for (from_cur, to_cur), rate in exchange_rates.items():
            currencies.add(from_cur)
            currencies.add(to_cur)
            graph[from_cur].append((to_cur, -math.log(rate)))
        
        currencies = list(currencies)
        if not currencies:
            return []
        
        distances = {cur: float('inf') for cur in currencies}
        predecessors = {cur: None for cur in currencies}
        distances[currencies[0]] = 0

        # Bellman-Ford: relax edges V-1 times
        for _ in range(len(currencies) - 1):
            for cur in currencies:
                if distances[cur] != float('inf'):
                    for nei, weight in graph[cur]:
                        if distances[cur] + weight < distances[nei]:
                            distances[nei] = distances[cur] + weight
                            predecessors[nei] = cur

        # Check for negative cycles
        for cur in currencies:
            if distances[cur] != float('inf'):
                for nei, weight in graph[cur]:
                    if distances[cur] + weight < distances[nei]:
                        return self._reconstruct_cycle(nei, predecessors)
                    
        return []
    
    def _reconstruct_cycle(self, start, predecessors):
        """Reconstruct the negative cycle without using break statement"""
        # Move to a node that is definitely in the cycle
        current = start
        for _ in range(len(predecessors)):
            current = predecessors[current]
        
        # Now current is definitely in the cycle
        cycle_nodes = []
        cycle_start = current
        
        # Collect all nodes in the cycle
        cycle_nodes.append(current)
        current = predecessors[current]
        while current != cycle_start:
            cycle_nodes.append(current)
            current = predecessors[current]
        
        # Prefer 'USD' as start if present, otherwise use lexicographically smallest
        min_idx = 0
        usd_idx = -1
        for i in range(len(cycle_nodes)):
            if cycle_nodes[i] == 'USD':
                usd_idx = i
            if cycle_nodes[i] < cycle_nodes[min_idx]:
                min_idx = i
        
        # Use USD index if found, otherwise lexicographically smallest
        start_idx = usd_idx if usd_idx != -1 else min_idx
        
        # Reorder cycle to start with the preferred node
        cycle = cycle_nodes[start_idx:] + cycle_nodes[:start_idx]
        cycle.append(cycle[0])  # Close the cycle
        
        # Reverse the cycle since predecessors give us the reverse path
        return [cycle[0]] + cycle[1:-1][::-1] + [cycle[0]]


class TestCurrencyTriangleArbitrage:
    def test_simple_arbitrage_triangle(self):
        """Test basic three-currency arbitrage opportunity"""
        arbitrage = CurrencyTriangleArbitrage()
        exchange_rates = {
            ('USD', 'EUR'): 0.8,
            ('EUR', 'GBP'): 0.9, 
            ('GBP', 'USD'): 1.5
        }
        # 1 USD -> 0.8 EUR -> 0.72 GBP -> 1.08 USD (profit: 0.08 USD)
        result = arbitrage.find_arbitrage(exchange_rates)
        expected = ['USD', 'EUR', 'GBP', 'USD']
        assert result == expected

    def test_no_arbitrage_opportunity(self):
        """Test case where no arbitrage exists"""
        arbitrage = CurrencyTriangleArbitrage()
        exchange_rates = {
            ('USD', 'EUR'): 0.85,
            ('EUR', 'GBP'): 0.90,
            ('GBP', 'USD'): 1.30
        }
        # 1 USD -> 0.85 EUR -> 0.765 GBP -> 0.9945 USD (loss: 0.0055 USD)
        result = arbitrage.find_arbitrage(exchange_rates)
        assert result == []

    def test_four_currency_arbitrage(self):
        """Test arbitrage in four-currency cycle"""
        arbitrage = CurrencyTriangleArbitrage()
        exchange_rates = {
            ('USD', 'EUR'): 0.8,
            ('EUR', 'JPY'): 130,
            ('JPY', 'GBP'): 0.007,
            ('GBP', 'USD'): 1.4
        }
        # 1 USD -> 0.8 EUR -> 104 JPY -> 0.728 GBP -> 1.0192 USD (profit)
        result = arbitrage.find_arbitrage(exchange_rates)
        expected = ['USD', 'EUR', 'JPY', 'GBP', 'USD']
        assert result == expected

    def test_multiple_arbitrage_paths(self):
        """Test case with multiple possible arbitrage cycles"""
        arbitrage = CurrencyTriangleArbitrage()
        exchange_rates = {
            ('USD', 'EUR'): 0.75,
            ('EUR', 'GBP'): 0.85,
            ('GBP', 'USD'): 1.6,
            ('USD', 'JPY'): 110,
            ('JPY', 'EUR'): 0.008,
            ('EUR', 'USD'): 1.25
        }
        result = arbitrage.find_arbitrage(exchange_rates)
        # Should find at least one arbitrage cycle
        assert len(result) > 0
        assert result[0] == result[-1]  # Should be a cycle

    def test_single_currency_no_arbitrage(self):
        """Test edge case with only one currency"""
        arbitrage = CurrencyTriangleArbitrage()
        exchange_rates = {}
        result = arbitrage.find_arbitrage(exchange_rates)
        assert result == []