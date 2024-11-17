//
//  LaunchesList.swift
//  HackUTD-SpaceXLaunches
//
//  Created by Nihaal Manesia on 11/11/24.
//

import SwiftUI

/// This will be our main launching point, we will create our list of launches here.
struct LaunchesList: View {
    var body: some View {
        NavigationStack {
            NavigationLink("Show me the details") {
                LaunchDetailView()
            }
        }
    }
}

#Preview {
    LaunchesList()
}
